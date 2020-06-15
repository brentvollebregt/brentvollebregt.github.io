import React, { useState } from "react";
import { navigate } from "@reach/router";
import { useStaticQuery, graphql } from "gatsby";
import ReactMarkdown from "react-markdown";
import { Helmet } from "react-helmet";
import unescape from "lodash/unescape";
import sideBarConfig from "../../../config/sidebar.json";
import "./SideBar.scss";

interface ICategories {
  name: string;
  postCount: number;
}

interface ICategoryPrefix {
  category: string;
  prefix: string;
}

interface IRecentVideos {
  title: string;
  thumbnailSrc: string;
  href: string;
}

interface IFeaturedSites {
  title: string;
  imageSrc: string;
  href: string;
}

const SideBar: React.FC = () => {
  const { allMarkdownRemark, recentYouTubeVideo } = useStaticQuery(graphql`
    query SidebarQuery {
      allMarkdownRemark(filter: { frontmatter: { templateKey: { eq: "blog-post" } } }) {
        edges {
          node {
            frontmatter {
              category
            }
          }
        }
      }
      recentYouTubeVideo {
        items {
          snippet {
            title
          }
          id {
            videoId
          }
        }
      }
    }
  `);

  const [searchQuery, setSearchQuery] = useState("");

  const onSearch = () => {
    if (searchQuery !== "") {
      navigate(`/search/?q=${encodeURIComponent(searchQuery)}`);
    }
  };

  const categoryOccurrences: string[] = allMarkdownRemark.edges.map(
    x => x.node.frontmatter.category
  );

  const about: string = sideBarConfig["about"];
  const categories: ICategories[] = categoryOccurrences
    .reduce((acc, category) => {
      const existing = acc.find(c => c.name === category);
      return [
        ...acc.filter(c => c.name !== category),
        existing !== undefined
          ? {
              name: category,
              postCount: existing.postCount + 1
            }
          : {
              name: category,
              postCount: 1
            }
      ];
    }, [] as ICategories[])
    .sort();
  const categoryPrefixes: ICategoryPrefix[] = sideBarConfig["categoryPrefixes"];
  const recentVideos: IRecentVideos[] = recentYouTubeVideo.items.map(v => ({
    title: unescape(v.snippet.title),
    thumbnailSrc: `https://img.youtube.com/vi/${v["id"]["videoId"]}/mqdefault.jpg`,
    href: `https://www.youtube.com/watch?v=${v["id"]["videoId"]}`
  }));
  const featuredSites: IFeaturedSites[] = sideBarConfig["featuredSites"];

  const getCategoryPrefix = (category: string) =>
    categoryPrefixes.find(c => c.category === category)?.prefix ?? "";

  return (
    <aside className="col-blog-sidebar blog-sidebar">
      <div className="card p-3 mb-3 bg-light about">
        <h4 className="text-center text-lg-left">About</h4>
        <ReactMarkdown source={about} />
      </div>

      <div className="input-group mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Search"
          aria-label="Search"
          value={searchQuery}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setSearchQuery(e.currentTarget.value)
          }
          onKeyDown={(event: React.KeyboardEvent<HTMLInputElement>) =>
            event.key === "Enter" && onSearch()
          }
        />
        <div className="input-group-append">
          <button className="btn btn-outline-primary" type="button" onClick={onSearch}>
            Search
          </button>
        </div>
      </div>

      <div className="card p-3 mb-3 bg-light">
        <h4 className="text-center text-lg-left">Categories</h4>
        <ol className="list-unstyled mb-0 text-center text-lg-left">
          {categories.map(({ name, postCount }) => (
            <li key={name}>
              <a href={`/blog/categories/#${name}`}>
                {getCategoryPrefix(name)} {name}
                <span className="badge badge-primary ml-3">{postCount}</span>
              </a>
            </li>
          ))}
        </ol>
      </div>

      <div className="card p-3 mb-3 bg-light">
        <h4 className="text-center text-lg-left">PyTutorials on YouTube</h4>
        <Helmet>
          <script async src="https://apis.google.com/js/platform.js"></script>
        </Helmet>
        <div style={{ textAlign: "center" }}>
          <div
            className="g-ytsubscribe"
            data-channel="PrivateSplat"
            data-layout="full"
            data-count="default"
          ></div>
        </div>
      </div>

      <div className="card p-3 mb-3 bg-light">
        <h4 className="text-center text-lg-left">Recent Videos</h4>
        <div className="yt-recent-video-container">
          {recentVideos.map(({ thumbnailSrc, href, title }) => (
            <img
              key={thumbnailSrc}
              src={thumbnailSrc}
              title={title}
              onClick={() => window.open(href, "_blank")}
            />
          ))}
        </div>
      </div>

      <div className="card p-3 mb-3 bg-light">
        <h4 className="text-center text-lg-left">Featured Sites</h4>
        <div className="featured-sites">
          {featuredSites.map(({ title, imageSrc, href }) => (
            <a key={title} title={title} href={href}>
              <img src={imageSrc} className="mw-100" />
            </a>
          ))}
        </div>
      </div>
    </aside>
  );
};

export default SideBar;
