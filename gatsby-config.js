module.exports = {
  siteMetadata: {
    siteUrl: `https://nitratine.net`,
    title: "Nitratine",
    blogFeed: {
      postsPerPage: 10,
      pagesEitherSideOfCurrentInPagination: 2
    }
  },
  plugins: [
    "gatsby-plugin-react-helmet",
    "gatsby-plugin-sass",
    {
      resolve: "gatsby-source-filesystem",
      options: {
        path: `${__dirname}/static/assets`,
        name: "uploads"
      }
    },
    {
      resolve: "gatsby-source-filesystem",
      options: {
        path: `${__dirname}/src/pages`,
        name: "pages"
      }
    },
    "gatsby-plugin-sharp",
    "gatsby-transformer-sharp",
    {
      resolve: "gatsby-transformer-remark",
      options: {
        tableOfContents: {
          heading: null,
          maxDepth: 3
        },
        plugins: [
          "gatsby-remark-images-anywhere", // Only supports one element/img per node/element. To get around this, wrap images that a beside each other in div tags
          {
            resolve: "gatsby-remark-autolink-headers",
            options: {
              offsetY: "60" // Header height (56) + a little more (4)
            }
          },
          {
            resolve: "gatsby-remark-relative-images",
            options: {
              name: "uploads"
            }
          },
          {
            resolve: "gatsby-remark-images",
            options: {
              // It's important to specify the maxWidth (in pixels) of
              // the content container as this plugin uses this as the
              // base for generating different widths of each image.
              maxWidth: 2048,
              disableBgImageOnAlpha: false
            }
          },
          {
            resolve: "gatsby-remark-copy-linked-files",
            options: {
              destinationDir: "static"
            }
          },
          {
            resolve: `gatsby-remark-prismjs`,
            options: {
              // This is used to allow setting a language for inline code
              // (i.e. single backticks) by creating a separator.
              // This separator is a string and will do no white-space
              // stripping.
              // A suggested value for English speakers is the non-ascii
              // character '›'.
              inlineCodeMarker: null,
              // This lets you set up language aliases.  For example,
              // setting this to '{ sh: "bash" }' will let you use
              // the language "sh" which will highlight using the
              // bash highlighter.
              aliases: {}
            }
          }
        ]
      }
    },
    "gatsby-plugin-typescript",
    {
      resolve: `gatsby-plugin-sitemap`,
      options: {
        query: `{
          site {
            siteMetadata {
              siteUrl
            }
          }
          allFile(filter: {extension: {eq: "md"}}) {
            edges {
              node {
                modifiedTime
                relativePath
              }
            }
          }
          allSitePage {
            nodes {
              path
            }
          }
        }`,
        serialize: ({ site, allFile, allSitePage }) =>
          allSitePage.nodes.map(node => {
            const filePresent = allFile.edges.find(
              item =>
                `/${item.node.relativePath.replace("index.md", "").replace(".md", "")}` ===
                node.path
            );
            return {
              url: `${site.siteMetadata.siteUrl}${node.path}`,
              lastmod: filePresent
                ? filePresent.node.modifiedTime.split("T")[0]
                : new Date().toISOString().split("T")[0]
            };
          })
      }
    },
    {
      resolve: "gatsby-plugin-netlify-cms",
      options: {
        modulePath: `${__dirname}/src/cms/cms.tsx`
      }
    }
    // {
    //   resolve: "gatsby-plugin-purgecss", // purges all unused/unreferenced css rules
    //   options: {
    //     develop: true, // Activates purging in npm run develop
    //     // purgeOnly: ["/all.scss"],
    //     whitelist: ["btn-primary"]
    //   }
    // } // must be after other CSS plugins
  ]
};
