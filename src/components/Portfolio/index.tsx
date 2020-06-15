import React from "react";
import useSyntaxHighlighter from "../../hooks/useSyntaxHighlighter";
import "./Portfolio.scss";

export interface IPortfolio {
  snippets: React.FC;
}

const Portfolio: React.FC<IPortfolio> = ({ snippets }) => {
  const highlightRoot = useSyntaxHighlighter();

  const Snippets = snippets;

  return (
    <div className="portfolio">
      <div className="col-xs-12 col-lg-8 d-block mx-auto">
        <h1 className="text-center">Portfolio</h1>
        <p className="lead text-center">
          This is a small collection of my favourite projects I developed with a small description
          and links to pages relating to the project.
        </p>
      </div>

      <div className="d-flex mw-100 masonry" ref={highlightRoot}>
        <Snippets />
      </div>
    </div>
  );
};

export default Portfolio;
