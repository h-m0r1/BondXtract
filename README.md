# BondXtract ⚛️

A browser-based tool for exploring and analyzing atomic bonds in crystal structures from CIF (Crystallographic Information File) format.

## Overview

BondXtract is a browser-based tool that helps researchers and crystallographers analyze atomic bonding patterns in crystal structures. The application reads CIF files and performs bond analysis with customizable search parameters.

## Features

### 🔍 **Advanced Bond Analysis**
- **Dual-atom bond search**: Specify two different atom types to find bonds between them
- **Distance-based filtering**: Set minimum and maximum distance ranges (in Ångströms)
- **Automatic optimization**: Mathematically optimized search ranges for efficient processing
- **Real-time progress tracking**: Monitor search progress with detailed status updates

### 📊 **Crystal Structure Support**
- **CIF file parsing**: Full support for Crystallographic Information File format
- **Space group symmetry**: Automatic detection and application of crystallographic symmetry operations
- **Embedded symmetry data**: Built-in space group data for 230 crystallographic space groups

### 🎯 **User-Friendly Interface**
- **Drag & drop support**: Easy file upload with visual feedback
- **Export functionality**: Download results as CSV files for further analysis

### ⚡ **Performance Features**
- **Progress monitoring**: Real-time search progress with ability to stop mid-process
- **Offline capable**: Works completely offline without internet connection

### 📦 **Portability**
- **Simple deployment**: Just place all application files in the same directory
- **No installation required**: Works immediately without any setup or configuration
- **Cross-platform**: Runs on any operating system with a modern web browser
- **Easy sharing**: Simply copy the files to share the application with others

## Usage

### Getting Started

1. **Setup the Application**
   - Place all application files (`BondXtract.html` and `embedded_spacegroups.js`) in the same directory
   - Open `BondXtract.html` in any modern web browser
   - No installation or server setup required

2. **Upload CIF File**
   - Drag and drop a CIF file onto the upload area, or
   - Click "Select File" to browse and select a CIF file

3. **Configure Search Parameters**
   - **Atom Types**: Select the two atom types you want to analyze
   - **Distance Range**: Set minimum and maximum bond distances
   - **Search Range**: Automatically optimized based on your distance settings

4. **Run Analysis**
   - Click "Search Bonds)" to start the analysis
   - Monitor progress in real-time
   - Use "Stop Search" or press Esc to stop mid-process

5. **Review Results**
   - View discovered bonds in the results table
   - Each bond shows atom types, coordinates, distance, and bond classification
   - Download results as CSV for external analysis

### Output Information

The tool provides detailed information for each discovered bond:
- **Atom 1 & Atom 2**: Element symbols and coordinates
- **Distance**: Bond length in Ångströms
- **Relative Position**: Spatial relationship between atoms
- **Bond Type**: Classification based on covalent radii

## Technical Details

### Supported File Formats
- **CIF (Crystallographic Information File)**: Standard format for crystallographic data
- **Space Groups**: All 230 crystallographic space groups supported
- **Atom Types**: All elements from the periodic table

### Browser Compatibility
- **Modern browsers**: Chrome, Firefox, Safari, Edge
- **No plugins required**: Pure HTML5, CSS3, and JavaScript
- **Offline capable**: Works completely offline without internet connection
- **No server required**: Runs entirely in the browser
- **Portable**: Simple directory deployment with no dependencies

## Current Status

**Planned Features**:
- Additional file format support
- Batch processing capabilities
- Ligand type identification (local molecular geometry analysis) - *low priority*
- Enhanced visualization options - *low priority*

## Contributing

Contributions are welcome! Areas for improvement include:
- Additional file format support
- Enhanced visualization features
- Performance optimizations
- Documentation improvements

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Hitoshi Mori** - 2025

## Acknowledgments

- Crystallographic community for CIF format standards
- Space group symmetry data sources
- Web development community for modern browser technologies

